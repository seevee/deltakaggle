<template>
  <div class="accepted">
    <p>Accepted</p>
    <ul>
      <p>Eligible Applicants by ID</p>
      <li v-for="(item, index) in data.items" v-bind:key="index">{{ item }}</li>
    </ul>
    <ul>
      <p>Eligible Applicants Statistics</p>
      <li v-for="(stat, index) in data.stats" v-bind:key="index">{{ stat }}</li>
    </ul>
    <button v-on:click="displayData();">Display Accepted</button>
  </div>
</template>

<script>
export default {
  name: 'DisplayAccepted',
  props: [
    'data'
  ],
}
</script>

<style>
</style>
