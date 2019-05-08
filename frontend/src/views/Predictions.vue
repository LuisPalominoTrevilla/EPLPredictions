<template>
    <div>
        <header class="color-wall">
            <h3>Predictions</h3>
        </header>
        <b-container>
            <v-fixture
                localName="Brighton and Hove Albion"
                localLogo="@/assets/Logos/BrightonHoveAlbion.png"
                awayName="Manchester City"
                awayLogo="@/assets/Logos/ManchesterCity.png"/>
        </b-container>
    </div>
</template>

<script>
import VFixture from '@/components/VFixture.vue';

export default {
  components: {
        VFixture
  }
}
</script>

<style lang="scss" scoped>
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
