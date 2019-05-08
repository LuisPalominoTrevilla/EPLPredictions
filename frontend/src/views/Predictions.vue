<template>
    <div>
        <header class="color-wall">
            <h3>Predictions</h3>
        </header>
        <b-container>
            <v-fixture
                class="mt-5"
                localName="Brighton and Hove Albion"
                localLogo="BrightonHoveAlbion.png"
                awayName="Manchester City"
                awayLogo="ManchesterCity.png"
                :matchStart="nextDate"
                :winner="1"/>
        </b-container>
    </div>
</template>

<script>
import moment from 'moment';
import VFixture from '@/components/VFixture.vue';

export default {
    components: {
        VFixture
    },

    computed: {
        nextDate() {
            return moment().add(4, 'days').toDate();
        }
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
