<script setup>
import {ref} from 'vue'
import {uplodafile} from "./apis/uploda.js";

const refuploda =ref()

const fileData = new FromData();


const fileuploda=()=>{
  fileData.append("filekeyname", refuploda.value.files[0]);

  console.log(fileData.get('filekeyname'))
  console.log(fileData)
}

const filesubmit= async ()=>{
  console.log("sigio ")
  const result = await uplodafile(fileData)
  console.log(result.data)
}


</script>

<template>
  <div>
    <input type="file" name="filename" class="uplodafileid" ref="refuploda" @change="fileuploda()">
    <button @click="filesubmit">提交</button>
  </div>
</template>