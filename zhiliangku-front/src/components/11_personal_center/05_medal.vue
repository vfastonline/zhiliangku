<template>
  <div>
    <div class="medal_title font1_34_6 ftc">已获得<span class="font1_34_b4">{{main_data.total || 0 }}</span>枚勋章</div>
    <CardContainer v-if="main_data.data" :config="{num:3,card:medal_unit,cardData:main_data.data[0]}">
      <medal_unit v-for="(item) in main_data.data" :key="item.id" :main_data="item"></medal_unit>
    </CardContainer>
  </div>
</template>

<script>
  import medal_unit from './10_medal_unit'
  import '../00_common/05_card_container'
  export default {
    name: "medal",

    data() {
      return {
        main_data: {},
        medal_unit:medal_unit
      }
    },
    methods: {},
    created() {
      this.$get("/medal/list/info").then(res => {
        console.log(res.data.data)
        if (!res.err) {
          // this.$fn.addString(this.$myConst.httpUrl, "res.data.data", "pathwel")
          this.main_data = res.data

        }
      })
    },
    components: {
      medal_unit: medal_unit,
    }
  }
</script>

<style scoped>
  .medal_title {
    margin-bottom: 70px;
  }
</style>
