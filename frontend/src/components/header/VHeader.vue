<template>
    <div>
        <img class="epl-logo" src="@/assets/premier-league-logo.png" alt="" :style="`width: ${imageWidth}rem`">
        <team-listing></team-listing>
        <v-menu
            @getOffset="getOffset"
            @addMargin="addMargin"/>
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
            margin: 0,
            imageWidth: 12
        };
    },

    methods: {
        addMargin(margin) {
            this.margin = margin;
        },

        getOffset(offset) {
            this.imageWidth = 3/28*offset+6;
        }
    }
}
</script>

<style lang="scss" scoped>
.epl-logo {
    z-index: 2;
    left: 0;
    top: 0;
    position: fixed;
}
</style>