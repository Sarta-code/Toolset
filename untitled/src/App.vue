<script setup>
import {ref} from 'vue'
import {uplodafile} from "./apis/uploda.js";
import Navigation from './layout/Navigation/index.vue'
import MainArea from './layout/Mainarea/index.vue'

const refuploda =ref()

const fileData = new FormData();


const fileUpLoad= async ()=>{

  for (let i = 0; i<refuploda.value.files.length; i++) {
    fileData.append(refuploda.value.files.item(i).name.split(".")[1]+'-'+refuploda.value.files.item(i).size, refuploda.value.files.item(i));
  }
  const result = await uplodafile(fileData)
  console.log(result.data)

}

const fileSubmit= async ()=>{
}


</script>

<template>
    <Navigation />
    <MainArea />
</template>
<style lang="css" scoped>
.csa{
  text-align: center;
}
</style>