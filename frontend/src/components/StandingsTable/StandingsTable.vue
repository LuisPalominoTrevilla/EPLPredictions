<script>
      import json from '@/prem_league_table.json'
      export default{
          data(){
              return{
                  myJson: json
              }
          },

          computed: {
                teamsLogos() {
                    return this.$store.state.teams.map(team => team+'.png')
                }
            },
            methods: {
                getImgUrl(pic) {
                    return require('@/assets/Logos/'+pic)
                }
            }
      }
</script>

<template>
    
</template>

<style lang="scss" scoped>

    .logo-container {
        padding: 0 .5rem;
        position: relative;
        height: 40px;
        width: 40px;
        float:left;
        padding:5px;
    }

    .team-logo {
        width: 2rem;
        cursor: pointer;
        position: absolute;
    }
    
    .table-bordered {
        border-top: 1px transparent;
        border-right: 1px transparent;
        border-bottom: 1px transparent;
        border-left: 1px transparent;
    }

    thead {
        color: gray;
    }

    th, td {
        border-bottom: 1px solid #ddd;
        border-top: 1px transparent;
        border-right: 1px transparent;
    }

    .teamdiv {
        border-right: 1px solid #ddd;
    }

    .color-wall {
    background-color: #eaff04;
    height: 7rem;
    display: flex;
    align-items: center;

    h3 {
        color: #38003c;
        font-size: 2rem;
        font-weight: bold;
        margin-left: 2rem;
    }
}
</style>