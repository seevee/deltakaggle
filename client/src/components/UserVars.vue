<template>
  <div class="boxes">
    <h1>{{ title }}</h1>
    <input v-model="inputMinAgeValue" id="inputMinAgeValue" /><label for="inputMinAgeValue"> Enter Minimum Age</label>
    <br>
    <input v-model="inputMaxAgeValue"/><label for="inputMaxAgeValue"> Enter Maximum Age</label>
    <br>
    <input v-model="inputMinIncomeValue"/><label for="inputMinIncomeValue"> Enter Minimum Monthly Income</label>
    <br>
    <input v-model="inputMaxUtilValue"/><label for="inputMaxUtilValue"> Enter Maximum Utilization of Revolving Credit</label>
    <br>
    <input v-model="inputThirtySixtyValue"/><label for="inputThirtySixtyValue"> Enter Maximum Number of 30 to 60 Day Deliquencies</label>
    <br>
    <input v-model="inputDebtRatioValue"/><label for="inputDebtRatioValue"> Enter Maximum Debt to Income Ratio</label>
    <br>
    <input v-model="inputMinLinesValue"/><label for="inputMinLinesValue"> Enter Minimum Number of Open Credit Lines</label>
    <br>
    <input v-model="inputNinetyValue"/><label for="inputNinetyValue"> Enter Maximum Number of Delinquencies over 90 Days</label>
    <br>
    <input v-model="inputMinRealEstateValue"/><label for="inputMinRealEstateValue"> Enter Minimum Number of Real Estate Loans or Lines</label>
    <br>
    <input v-model="inputMaxSixtyNinetyValue"/><label for="inputMaxSixtyNinetyValue"> Enter Maximum Number of 60 to 90 Day Delinquencies</label>
    <br>
    <input v-model="inputMaxDependentsValue"/><label for="inputMaxDependentsValue"> Enter Maximum Number of Dependents</label>
    <br>
    <button v-on:click="enterAccepted()">Submit Variables to Accept Applications</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'UserVars',
  props: ['title'],

  data () {
    return {
      age_range: [],
      min_income: [],
      max_revolving: [],
      max_thirtysixty: [],
      max_debtratio: [],
      min_openlines: [],
      max_ninety: [],
      min_realestate: [],
      max_sixtyninety: [],
      max_dependents: [],
      eligible_applicants: [],
      inputMinAgeValue: '',
      inputMaxAgeValue: '',
      inputMinIncomeValue: '',
      inputMaxUtilValue: '',
      inputThirtySixtyValue: '',
      inputDebtRatioValue: '',
      inputMinLinesValue: '',
      inputNinetyValue: '',
      inputMinRealEstateValue: '',
      inputMaxSixtyNinetyValue: '',
      inputMaxDependentsValue: '',
    }
  },
  methods: {
    async enterAccepted() {
      this.age_range.push(this.inputMinAgeValue)
      this.age_range.push(this.inputMaxAgeValue)
      this.min_income.push(this.inputMinIncomeValue)
      this.max_revolving.push(this.inputMaxUtilValue)
      this.max_thirtysixty.push(this.inputThirtySixtyValue)
      this.max_debtratio.push(this.inputDebtRatioValue)
      this.min_openlines.push(this.inputMinLinesValue)
      this.max_ninety.push(this.inputNinetyValue)
      this.min_realestate.push(this.inputMinRealEstateValue)
      this.max_sixtyninety.push(this.inputMaxSixtyNinetyValue)
      this.max_dependents.push(this.inputMaxDependentsValue)
      const result = await axios.post('user_vars', { age_item: this.age_range, income_item: this.min_income, util_item: this.max_revolving, thirtysixty_item: this.max_thirtysixty,
        debtratio_item: this.max_debtratio, minlines_item: this.min_openlines, ninety_item: this.max_ninety, 
        realestate_item: this.min_realestate, sixtyninety_item: this.max_sixtyninety, dependents_item: this.max_dependents})
      console.log(result.data)
      this.$emit('dataEntered', result.data)
    },
  }
}
</script>
<style>
.boxes {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  width: 100%;
  text-align: right;
  margin: 10% 0;
  min-height: 200px;
  background-color: rgba(33, 33, 33, .3);
  align-items: center;
}

.boxes :first-child {
  align-self: center;
}
</style>
