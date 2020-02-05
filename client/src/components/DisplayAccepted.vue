<template>
  <div class="accepted">
    <p>Accepted</p>
    <ul>
      <p>Eligible Applicants by ID</p>
      <li v-for="items in data.items" v-bind:key="items">{{ items }}</li>
    </ul>
    <ul>
      <p>Eligible Applicants Statistics</p>
      <li v-for="stats in data.stats" v-bind:key="stats">{{ stats }}</li>
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
