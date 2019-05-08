<template>
    <carousel :perPage="4">
        <slide v-for="(logo, idx) in teamsLogos" :key="idx" class="text-center">
            <img class="team-logo" :src="getImgUrl(logo)" alt="" @click="selectTeam(logo.split('.png')[0])">
        </slide>
    </carousel>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel';

export default {
    components: {
        Carousel,
        Slide
    },

    computed: {
        teamsLogos() {
            return this.$store.state.teams.map(team => team+'.png')
        }
    },

    methods: {
        getImgUrl(pic) {
            return require('@/assets/Logos/'+pic)
        },

        selectTeam(teamName) {
            const team = {
                name: teamName.replace(/([A-Z])/g, ' $1').trim(),
                logo: `${teamName}.png`
            }
            this.$emit('selected', team);
        }
    }
}
</script>

<style lang="scss" scoped>
.team-logo {
    width: 4rem;
    cursor: pointer;
}
</style>
