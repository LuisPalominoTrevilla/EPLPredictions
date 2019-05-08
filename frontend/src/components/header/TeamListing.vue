<template>
    <b-container class="logos-container">
        <div v-for="(logo, idx) in teamsLogos" :key="idx" class="logo-container">
            <img class="team-logo" :src="getImgUrl(logo)" alt="">
        </div>
    </b-container>
</template>

<script>
export default {
    data() {
        return {

        };
    },

    beforeMount() {
        console.log();
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
.logos-container {
    padding-top: .5rem;
    padding-bottom: .5rem;
    display: flex;
    justify-content: space-evenly;
    align-items: center;

    .logo-container {
        padding: 0 .5rem;
        position: relative;
        height: 40px;
    }

    .team-logo {
        width: 2rem;
        cursor: pointer;
        position: absolute;

        &:hover {
            width: 2.3rem;
            transition: .3s;
        }
    }
}
</style>