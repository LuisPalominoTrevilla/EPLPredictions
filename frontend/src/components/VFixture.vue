<template>
    <b-row>
        <b-col>
            {{ localName }}
        </b-col>
        <b-col>
            {{ awayName }}
        </b-col>
    </b-row>
</template>

<script>

export default {
    props: {
        localName: {
            type: String,
            required: true
        },
        localLogo: {
            type: String,
            required: true
        },
        awayName: {
            type: String,
            required: true
        },
        awayLogo: {
            type: String,
            required: true
        }
    }
}
</script>

<style lang="scss" scoped>

</style>
