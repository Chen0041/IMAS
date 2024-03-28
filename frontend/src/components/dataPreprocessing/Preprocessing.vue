<template>
  <el-container>
    <el-header style="height: 80px; width: 95vw">
      <NavigationBar/>
    </el-header>
    <el-main style="height: calc(100vh - 80px); width: 95vw">
      <div style="display: flex; justify-content: center;">

      </div>
    </el-main>
  </el-container>
</template>


<script>
import NavigationBar from "@/components/NavigationBar.vue";

export default {
  name: "preprocessing",
  components: {
    NavigationBar
  },

}
</script>


<style scoped>

</style>