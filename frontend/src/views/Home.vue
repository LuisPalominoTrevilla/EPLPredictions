<template>
  <div id="textExample">
    <header class="color-wall">
        <h3>Premiere League Standings</h3>
    </header>
    <table class="table">
                <thead>
                    <tr>
                        <th> Position</th>
                        <th> Club</th>
                        <th> Played</th>
                        <th> Won</th>
                        <th> Drawn</th>
                        <th> Lost</th>
                        <th> GF</th>
                        <th> GA</th>
                        <th> GD</th>
                        <th> Points</th>
                    </tr>
                </thead>
                <tr v-for="data in myJson.Data.tables[0].table" v-bind:key="data">
                    <td>{{data.positionOverall}}</td>
                    <td class="teamdiv">
                        <div class="logo-container">
                            <img class="team-logo" :src="getImgUrl(data.teamImg)" alt="">
                        </div>
                        {{data.teamName}}
                    </td>
                    <td>{{data.playedTotal}}</td>
                    <td>{{data.winTotal}}</td>
                    <td>{{data.drawTotal}}</td>
                    <td>{{data.lossTotal}}</td>
                    <td>{{data.goalsForTotal}}</td>
                    <td>{{data.goalsAgainstTotal}}</td>
                    <td>{{data.goalDifferenceTotal}}</td>
                    <td>{{data.pointsOverall}}</td>
                </tr>
            </table>
    </div>
</template>

<script>
import json from '@/prem_league_table.json'

export default {
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

<style lang="scss" scoped>
  .home {
    text-align: center;
  }
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