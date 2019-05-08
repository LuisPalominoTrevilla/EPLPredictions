<template>
    <div>
        <img class="epl-logo" src="@/assets/premier-league.png" alt="">
        <team-listing></team-listing>
        <v-menu @addMargin="addMargin"/>
        <div :style="`margin-bottom: ${margin}px`"></div>
    </div>
</template>

<script>
import VMenu from './VMenu.vue';
import TeamListing from './TeamListing.vue';

export default {
    components: {
        VMenu,
        TeamListing
    },

    data() {
        return {
            margin: 0
        };
    },

    methods: {
        addMargin(margin) {
        this.margin = margin;
        }
    }
}
</script>

<style lang="scss" scoped>
.epl-logo {
    width: 7rem;
    z-index: 2;
    left: 0;
    top: 0;
    position: fixed;
}
</style>