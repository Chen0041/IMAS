<template>
  <div>
    <el-container>
      <NavigationBar/>
      <el-container>
        <el-main>
          <div class="kg-div">
            <div class="svg-div" ref="svgDiv">
              <svg width="100%" height="100%">
              </svg>
            </div>
          </div>
          <div class="search-bar">
            <el-input placeholder="Search Node" v-model="searchContent" clearable>
              <el-button slot="append" icon="el-icon-search" @click="searchNode"></el-button>
            </el-input>
          </div>
          <div class="info-div">
            <el-card shadow="never">
              <div slot="header" class="">
                <span>Statistics</span>
              </div>
              <div>
                <span>All nodes: <em>{{statistics.numOfNodes}}</em></span><br/><br/>
                <span>Patients: <em>{{statistics.numOfPatients}}</em></span><br/>
                <span>Admissions: <em>{{statistics.numOfAdmissions}}</em></span><br/>
                <span>Diseases: <em>{{statistics.numOfDiseases}}</em></span><br/>
                <span>Drugs: <em>{{statistics.numOfDrugs}}</em></span><br/><br/>
                <span>Edges: <em>{{statistics.numOfEdges}}</em></span><br/>
              </div>
            </el-card>
          </div>
          <div class="option-div">
            <el-card shadow="never">
              <div slot="header" class="">
                <span>Display Options</span>
              </div>
              <div>
                <el-switch
                  v-model="displayPatient"
                  active-text="Patients"
                  @change="patientSwitchChange">
                </el-switch>
                <br/>
                <el-switch
                  v-model="displayAdmission"
                  active-text="Admissions"
                  @change="admissionSwitchChange">
                </el-switch>
                <br/>
                <el-switch
                  v-model="displayDisease"
                  active-text="Diseases"
                  @change="diseaseSwitchChange">
                </el-switch>
                <br/>
                <el-switch
                  v-model="displayDrug"
                  active-text="Drugs"
                  @change="drugSwitchChange">
                </el-switch>
              </div>
            </el-card>
            
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
<script>
    import NavigationBar from "../components/NavigationBar.vue";

    import * as d3 from 'd3';
    // import d3tooltip from 'd3-tooltip';

    import GraphData from "../assets/GraphData";

    export default {
        name: "knowledgeGraph",
        components: {
            NavigationBar
        },
        data() {
            return {
                kgGroupList: [{
                    label: 'System Knowledge Graph',
                    options: []
                }, {
                    label: 'My Knowledge Graph',
                    options: []
                }],
                kgChosen: '',
                kgSvgComponents: {
                    svg: null,
                    simulation: null,
                    colors: [],

                    linkGroup: [],
                    linkTextGroup: [],
                    nodeGroup: [],
                    nodeTextGroup: []
                },
                kgNodeBufferedMap: [],
                kgNodeUnfoldFlag: [],
                kgEntityInfo: {
                    entityType: 'Entity Info',
                    id: -1,
                    name: '',
                    childNode: [],
                    noChildNodeInfo: '',
                    status: true
                },
                kgData: {
                    nodes: [],
                    links: []
                },


                kgNodeMap: [],
                kgNodeChildMap: [],
                bufferedChildEntities: {
                    nodes: [],
                    links: []
                },
                searchContent: '',
                transform: '',
                statistics: {},
                displayPatient: true,
                displayAdmission: true,
                displayDisease: true,
                displayDrug: false,
                hideNode: ["drug"]
            };
        },
        beforeMount: function() {
          this.kgChosen = 0
          this.loadKG()
          this.$axios({
              method: 'get',
              url: '/kg/statistics/',
          }).then(res => {
              this.statistics = res.data
          }).catch(error => {
              console.log(error);
          });
        },
        methods: {
            loadKGList() {
                this.$axios({
                    method: 'get',
                    url: '/kg/user/' + this.$store.state.user.id,
                }).then(res => {
                    this.kgGroupList[1].options.length = 0;
                    for (let kg in res.data) {
                        if (res.data.hasOwnProperty(kg)) {
                            this.kgGroupList[1].options.push({
                                value: res.data[kg].id,
                                label: res.data[kg].name
                            });
                        }
                    }
                }).catch(error => {
                    console.log(error);
                });
            },
            loadKG() {
              this.removeCurrentKgData();
              this.$axios({
                  method: 'get',
                  url: '/kg/graph',
              }).then(res => {
                  let nodes = res.data.nodes;
                  let links = res.data.links;
                  this.kgData.nodes = nodes;
                  this.kgData.links = links;
                  for (let node in nodes) {
                      if (nodes.hasOwnProperty(node)) {
                          this.kgNodeBufferedMap[nodes[node].id] = {
                              id: nodes[node].id,
                              name: nodes[node].name,
                              childNode: [],
                              relations: [],
                              loadedInGraph: true
                          };
                      }
                  }
                  for (let link in links) {
                      if (links.hasOwnProperty(link)) {
                          this.kgNodeBufferedMap[links[link].source].childNode.push({
                              id: this.kgNodeBufferedMap[links[link].target].id,
                              name: this.kgNodeBufferedMap[links[link].target].name
                          });
                          this.kgNodeBufferedMap[links[link].source].relations.push(links[link]);
                          this.kgNodeUnfoldFlag[links[link].source] = false;
                          this.kgNodeUnfoldFlag[links[link].target] = true;
                      }
                  }
                  this.paintGraph();
              }).catch(error => {
                  console.log(error);
              });
            },
            searchNode(){
              this.removeCurrentKgData();
              this.$axios({
                  method: 'get',
                  url: '/kg/node/search/' + this.searchContent,
              }).then(res => {
                  let nodes = res.data.nodes;
                  let links = res.data.links;
                  this.kgData.nodes = nodes;
                  this.kgData.links = links;
                  for (let node in nodes) {
                      if (nodes.hasOwnProperty(node)) {
                          this.kgNodeBufferedMap[nodes[node].id] = {
                              id: nodes[node].id,
                              name: nodes[node].name,
                              childNode: [],
                              relations: [],
                              loadedInGraph: true
                          };
                      }
                  }
                  for (let link in links) {
                      if (links.hasOwnProperty(link)) {
                          this.kgNodeBufferedMap[links[link].source].childNode.push({
                              id: this.kgNodeBufferedMap[links[link].target].id,
                              name: this.kgNodeBufferedMap[links[link].target].name
                          });
                          this.kgNodeBufferedMap[links[link].source].relations.push(links[link]);
                          this.kgNodeUnfoldFlag[links[link].source] = false;
                          this.kgNodeUnfoldFlag[links[link].target] = true;
                      }
                  }
                  this.paintGraph();
              }).catch(error => {
                  console.log(error);
              });
            },
            removeCurrentKgData() {
                this.kgNodeBufferedMap.length = 0;
                this.kgNodeUnfoldFlag.length = 0;
                this.kgEntityInfo.entityType = 'Entity Info';
                this.kgEntityInfo.id = -1;
                this.kgEntityInfo.name = '';
                this.kgEntityInfo.childNode.length = 0;
                this.kgEntityInfo.noChildNodeInfo = '';
                this.kgData.nodes.length = 0;
                this.kgData.links.length = 0;
            },
            displayNodeInfo(nodeId) {
                this.kgEntityInfo.entityType = 'Node';
                this.kgEntityInfo.id = nodeId;
                this.kgEntityInfo.name = this.kgNodeBufferedMap[nodeId].name;
                let childNode = this.kgNodeBufferedMap[nodeId].childNode;
                if (childNode != null) {
                  if (childNode.length === 0) {
                    this.kgEntityInfo.noChildNodeInfo = 'Loading...';
                    this.getRelNodes(nodeId);
                  } else {
                    this.kgEntityInfo.childNode = childNode;
                    if (this.kgNodeUnfoldFlag[this.kgEntityInfo.id]) {
                      this.unfoldRelNodes()
                    }
                  }
                } else {
                  this.kgEntityInfo.noChildNodeInfo = 'No relation node';
                }
            },
            getRelNodes(nodeId) {
                if (this.kgNodeBufferedMap[nodeId].childNode.length === 0) {
                    this.$axios({
                        method: 'get',
                        url: '/kg/graph/relNodes/' + nodeId,
                    }).then(res => {
                        let nodes = res.data.nodes;
                        let links = res.data.links;
                        this.kgNodeBufferedMap[nodeId].childNode = nodes;
                        this.kgNodeBufferedMap[nodeId].relations = links;
                        this.kgEntityInfo.childNode = nodes;
                        for (let node in nodes) {
                            if (nodes.hasOwnProperty(node)) {
                                if (this.kgNodeBufferedMap[nodes[node].id] == null) {
                                    this.kgNodeBufferedMap[nodes[node].id] = {
                                        id: nodes[node].id,
                                        name: nodes[node].name,
                                        childNode: [],
                                        relations: [],
                                        loadedInGraph: false
                                    };
                                    this.kgNodeUnfoldFlag[nodes[node].id] = true;
                                }
                            }
                        }
                        if (this.kgNodeUnfoldFlag[this.kgEntityInfo.id]) {
                          this.unfoldRelNodes()
                        }
                    }).catch(error => {
                        console.log(error);
                    });
                }
            },
            unfoldRelNodes() {
                let newNodes = this.kgNodeBufferedMap[this.kgEntityInfo.id].childNode;
                for (let node in newNodes) {
                    if (newNodes.hasOwnProperty(node)) {
                        let n = newNodes[node];
                        if (!this.kgNodeBufferedMap[n.id].loadedInGraph) {
                            this.kgData.nodes.push(n);
                            this.kgNodeBufferedMap[n.id].loadedInGraph = true;
                        }
                    }
                }
                // 这里可能会出现重复的link，使用linkSet去重是否有效？无效 因为link的source和target互换了
                let links = this.kgData.links.concat(this.kgNodeBufferedMap[this.kgEntityInfo.id].relations);
                let linkSet = new Set(links);
                this.kgData.links = Array.from(linkSet);
                this.paintGraph();
                this.kgNodeUnfoldFlag[this.kgEntityInfo.id] = false;
            },
            ellipsisRelNodes() {
            },
            resetGraph() {
                this.loadKG();
            },
            initGraph() {
                // console.log("Init Graph SVG");
                let width = this.$refs.svgDiv.offsetWidth;
                let height = this.$refs.svgDiv.offsetHeight;
                this.kgSvgComponents.simulation = d3.forceSimulation()
                    .force("link", d3.forceLink().id(d => {return d.id;}))
                    .force("charge", d3.forceManyBody().strength(100))
                    .force("center", d3.forceCenter(width / 2, height / 2))
                    .force("collide", d3.forceCollide(80).strength(0.2).iterations(5));
                this.kgSvgComponents.colors = [
                    '#6ca46c', '#4e88af',
                    '#ca635f', '#d2907c',
                    '#d6744d', '#cec255',
                    '#b4c6e7', '#cdb4e6'
                ];
                this.kgSvgComponents.svg = d3.select("svg");
                this.kgSvgComponents.linkGroup = this.kgSvgComponents.svg.append("g").attr("class", "links");
                this.kgSvgComponents.nodeGroup = this.kgSvgComponents.svg.append("g").attr("class", "nodes");
                this.kgSvgComponents.nodeTextGroup = this.kgSvgComponents.svg.append("g").attr("class", "texts");
            },
            paintGraph() {
                let svg = this.kgSvgComponents.svg;
                let simulation = this.kgSvgComponents.simulation;
                let colors = this.kgSvgComponents.colors;

                svg.selectAll("*").remove();
                let centerX = this.$refs.svgDiv.offsetWidth / 2;
                let centerY = this.$refs.svgDiv.offsetHeight / 2;

                let link = svg.append("g").attr("class", "links")
                    .selectAll("line").data(this.kgData.links.filter((link) => {
                        for (const node of this.kgData.nodes) {
                            if (this.hideNode.includes(node.type) && (node.id == link.target.id || node.id == link.source.id)) {
                                return false;
                            }
                        }
                        return true;
                    })).enter().append("line")
                    .attr("stroke-width", 1)
                    .style("stroke", "rgba(240, 240, 240, 0.8)");

                let tooltip = d3.select("body").select(".tooltip")
                if (tooltip._groups[0][0] == null) {
                    tooltip = d3.select("body").append("div")
                    .attr("class", "tooltip")
                    .style("display", "none")
                    .style("color", "#ffffff")
                    .style("background-color", "#303133")
                    .style("text-align", "center")
                    .style("border", "1px solid #303133")
                    .style("border-radius", "4px")
                    .style("padding", "10px 20px")
                    .style("width", "fit-content")
                    .style("position", "relative")                    
                    .style("white-space", "pre")
                    .style("box-shadow", "2px 2px 2px #202020");
                }

                function setTooltipContent(d) {
                  let content = '';
                  if (d.type == "patient") {
                        content += "patient_id: " + d.patient_id + "\n"
                        content += "gender: " + d.gender + "\n"
                        content += "religion: " + d.religion + "\n"
                        content += "ethnicity: " + d.ethnicity + "\n"
                        content += "birth_time: " + d.birth_time + "\n"                   
                      } else if (d.type == "admission") {
                        content += "admission_id: " + d.admission_id + "\n"
                        content += "admit_time: " + d.admit_time + "\n"
                        content += "duration: " + d.duration + "\n"
                        content += "flag: " + d.flag + "\n"
                        content += "admit_age: " + d.admit_age + "\n"
                      } else if (d.type == "disease") {
                        content += "disease_id: " + d.disease_id + "\n"
                        content += "alias: " + d.alias + "\n"
                      } else if (d.type == "drug") {
                        content += "drug_id: " + d.drug_id + "\n"
                        content += "drug_alias: " + d.drug_alias + "\n"
                        content += "dose_val_rx: " + d.dose_val_rx + "\n"
                        content += "dose_unit_rx: " + d.dose_unit_rx + "\n"
                      }
                  return content;
                }
                var that = this;
                function nodeCheck(node) {
                    return !that.hideNode.includes(node.type)
                }
                function updateTooltip(d) {
                    tooltip.html(setTooltipContent(d))
                        .style("left", (d3.event.pageX) + "px")
                        .style("top", (d3.event.pageY - tooltip.node().getBoundingClientRect().height * 0.5) + "px");
                }
                let node = svg.append("g").attr("class", "nodes")
                    .selectAll("circle").data(this.kgData.nodes.filter(nodeCheck)).enter().append("circle")
                    .attr("cx", centerX)
                    .attr("cy", centerY)
                    .attr("r", d => {return 50;})
                    .attr("fill", d => {
                        if (d.type == "patient") {
                            return colors[0]
                        } else if (d.type == "admission") {
                            return colors[1]
                        } else if (d.type == "disease") {
                            return colors[2]
                        } else if (d.type == "drug") {
                            return colors[5]
                        }
                    })
                    .style("stroke", "#fff")
                    .style("stroke-width", "2px")
                    .style("cursor", "pointer")
                    .call(d3.drag().on("start", dragstarted).on("drag", dragged).on("end", dragended))
                    .on('mouseover', function (d, i) {
                        tooltip.style("display", "block")
                        .style("color", "#ffffff")
                        .style("background-color", "#303133")
                        .style("border", "1px solid #303133")
                        .style("box-shadow", "2px 2px 2px #202020");
                        updateTooltip(d);
                    })
                    .on('mousemove', function (d, i) {
                        updateTooltip(d);
                    })
                    .on('mouseout', function (d, i) {
                        tooltip.style("display", "none");
                    });

                node.on("click", d => {
                    this.displayNodeInfo(d.id);
                });

                let text = svg.append("g").attr("class", "texts")
                    .selectAll("text").data(this.kgData.nodes.filter(nodeCheck)).enter().append("text")
                    .text(d => {
                      if (d.type == "patient") {
                        return "patient " + d.patient_id
                      } else if (d.type == "admission") {
                        return "admission " + d.admission_id
                      } else if (d.type == "disease") {
                        return d.alias
                      } else if (d.type == "drug") {
                        return d.drug_alias
                      }
                    })
                    .attr("x", centerX)
                    .attr("y", centerY)
                    .attr("text-anchor", "middle")
                    .attr("fill", "white")
                    .style("cursor", "pointer")
                    .call(d3.drag().on("start", dragstarted).on("drag", dragged).on("end", dragended))
                    .on('mouseover', function (d, i) {
                        tooltip.style("display", "block")
                        .style("color", "#ffffff")
                        .style("background-color", "#303133")
                        .style("border", "1px solid #303133")
                        .style("box-shadow", "2px 2px 2px #202020");
                        updateTooltip(d);
                    })
                    .on('mousemove', function (d, i) {
                        updateTooltip(d);
                    })
                    .on('mouseout', function (d, i) {
                        tooltip.style("display", "none");
                    })
                    .call(wrap);
                
                function wrap(text) {
                    text.each(function() {
                        var text = d3.select(this);
                        var words = text.text().split(/\s+|\*|-/).reverse();
                        var word;
                        var x = text.attr("x");
                        var y = text.attr("y");
                        var dy = 5;
                        var lines = [];
                        var line = [];
                        var lineNumber = 0;
                        var lineHeight = 18;

                        while (word = words.pop()) {
                            line.push(word);
                            if (line.join(" ").length > 9) {
                                if (line.length == 1) {
                                    lines.push(line.join(" "));
                                    line.pop();
                                } else {
                                    line.pop();
                                    lines.push(line.join(" "));
                                    line = [word];
                                }
                            }
                        }
                        if (line.length != 0) {
                            lines.push(line.join(" "));
                        }

                        text.text(null)
                        dy = dy + lineHeight * (1 - lines.length) * 0.5 // calculate actual offset of y
                        for (let index = 0; index < lines.length; index++) {
                            const element = lines[index];
                            text.append("tspan")
                                .attr("x", x)
                                .attr("y", y)
                                .attr("dy", lineNumber++ * lineHeight + dy)
                                .text(element);
                        }
                    })
                }

                var tspan = svg.selectAll("tspan");

                text.on("click", d => {
                    this.displayNodeInfo(d.id);
                });

                svg.selectAll("g").attr("transform", this.transform);

                simulation.nodes(this.kgData.nodes.filter(nodeCheck)).on("tick", ticked);
                simulation.force("link").links(this.kgData.links.filter((link) => {
                    for (const node of this.kgData.nodes) {
                        if (this.hideNode.includes(node.type) && (node.id == link.target || node.id == link.source)) {
                            return false;
                        }
                    }
                    return true;
                }));
                simulation.alpha(0.1).restart();
                svg.call(d3.zoom().on("zoom", () => {
                    svg.selectAll("g").attr("transform", d3.event.transform);
                    this.transform = d3.event.transform;
                }));
                svg.on("dblclick.zoom", null);
                function ticked() {
                    link
                        .attr("x1", function(d) {return d.source.x;})
                        .attr("y1", function(d) {return d.source.y;})
                        .attr("x2", function(d) {return d.target.x;})
                        .attr("y2", function(d) {return d.target.y;});
                    node
                        .attr("cx", function(d) {return d.x;})
                        .attr("cy", function(d) {return d.y;});
                    text
                        .attr("x", function(d) { return d.x; })
                        .attr("y", function(d) { return d.y; });
                    tspan
                        .attr("x", function(d) { return d.x; })
                        .attr("y", function(d) { return d.y; });
                }
                function dragstarted(d) {
                    if (!d3.event.active) simulation.alphaTarget(0.2).restart();
                    d.fx = d.x;
                    d.fy = d.y;
                }
                function dragged(d) {
                    d.fx = d3.event.x;
                    d.fy = d3.event.y;
                }
                function dragended(d) {
                    if (!d3.event.active) simulation.alphaTarget(0);
                    d.fx = null;
                    d.fy = null;
                }
            },
            downloadKg() {
            },
            patientSwitchChange(bool) {
              this.switchChange(bool, "patient")
            },
            admissionSwitchChange(bool) {
              this.switchChange(bool, "admission")
            },
            diseaseSwitchChange(bool) {
              this.switchChange(bool, "disease")
            },
            drugSwitchChange(bool) {
              this.switchChange(bool, "drug")
            },
            switchChange(bool, type) {
              if (bool) {
                this.hideNode.splice(this.hideNode.indexOf(type), 1);
              } else {
                this.hideNode.push(type);
              }
              this.paintGraph()
            }
        },
        created() {
            this.loadKGList();
        },
        mounted() {
            this.initGraph();
        }
    }
</script>

<style scoped>
  .el-main {
    position: fixed;
    top: 80px;
    left: 30px;
    right: 30px;
    bottom: 0;
    margin: 20px;
    padding: 10px;
  }

  .option-bar {
    /*text-align: center;*/
    float: left;
  }

  .option-block {
    display: inline-block;
    /*margin-right: 40px;*/
  }

  .option-block .el-select {
    width: 400px;
  }

  .btn-div {
    float: right;
  }

  .kg-div {
    position: fixed;
    /* top: 160px; */
    top: 100px;
    left: 30px;
    /* right: 360px; */
    right: 320px;
    bottom: 0;
    margin: 20px;
    border: 3px solid #272b30;
    border-radius: 8px;
    padding: 10px;
  }

  .info-div {
    position: fixed;
    top: 130px;
    right: 30px;
    /*bottom: 0;*/
    width: 250px;
    margin: 10px;
    /*margin: 20px;*/
    padding-top: 10px;
  }

  .svg-div {
    width: 100%;
    height: 100%;
    /*background-color: cadetblue;*/
  }

  svg {
    background-color: #272b30;
    border-radius: 4px;
  }

  .search-bar {
    position: fixed;
    top: 100px;
    right: 50px;
    width: 250px;
  }
  
  .option-div {
    position: fixed;
    top: 400px;
    right: 30px;
    width: 250px;
    margin: 10px;
  }
  
  .option-div .el-switch:not(:last-child) {
    padding-bottom: 10px;
  }
</style>
