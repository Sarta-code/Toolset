<script setup>
import {ref} from 'vue'
import {uplodafile} from "./apis/uploda.js";

const refuploda =ref()

const fileData = new FormData();


const fileUpLoad=()=>{

  for (let i = 0; i<refuploda.value.files.length; i++) {
    fileData.append(refuploda.value.files.item(i).name.split(".")[1]+'-'+refuploda.value.files.item(i).size, refuploda.value.files.item(i));
  }
}

const fileSubmit= async ()=>{
  console.log("sigio ")
  const result = await uplodafile(fileData)
  console.log(result.data)
}


</script>

<template>
  <div>
    <input type="file" name="filename" multiple class="uplodafileid" ref="refuploda" @change="fileUpLoad()">
    <button @click="fileSubmit">提交</button>
  </div>
</template>