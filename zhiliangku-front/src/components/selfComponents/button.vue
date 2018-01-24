<template>
  <div>
      <button @click="jj()">request</button>
      <button @click="hh()">antho</button>
  </div>
</template>
<script>
//首先这个面页会实例化出来vue，我觉得应该适当简化main.js

    export default{
        data(){
            return{

            }
        },
        methods:{
            jj(){
                this.$get('/slides/list',{method:'post',data:{usernaem:'18500390490',password:'123'}}).then(res=>{
                    console.log(res)
                })
            },
            hh(){
                this.$post('/customuser/login',{usernaem:'18500390490',password:'123'}).then(res=>{
                    console.log(res)
                })
            }
        },
        created(){
            this.$on('err',res=>{
                console.log(res)
                console.log(this)
                
            })
        }
    }
</script>
