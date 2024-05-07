<template>
  <el-aside width="240px" class="scrollable-div">
    <el-scrollbar ref="vqaMenuScrollBar">
      <el-menu
          router
          @select=""
          @open=""
          @close=""
          :default-active="this.$route.path">
        <el-menu-item index="/modelTrain/new">New Train Task</el-menu-item>
        <el-menu-item index="/modelTrain/report">Download Report</el-menu-item>
      </el-menu>
    </el-scrollbar>
  </el-aside>
</template>

<script>
    export default {
        data() {
            return {
                category: []
            };
        },
        methods: {
        },
        created() {
        }
    }
</script>

<style scoped>
    .el-aside {
        position: fixed;
        top: 80px;
        bottom: 0;
        background-color: rgb(238, 241, 246);
        z-index: 999;
    }

    .el-scrollbar {
        height: 100%;
    }
</style>
