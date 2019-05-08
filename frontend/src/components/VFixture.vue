<template>
    <div>
        <b-row class="fixture">
            <b-col>
                <img class="team-logo" :src="getImgUrl(localLogo)" alt="">
                {{ localName }}
            </b-col>
            <b-col class="text-center matchDate">
                {{ formatedDate }}
            </b-col>
            <b-col class="text-right">
                {{ awayName }}
                <img class="team-logo" :src="getImgUrl(awayLogo)" alt="">
            </b-col>
        </b-row>
        <b-row class="result pt-4">
            <b-col cols="12" class="text-center">
                <h4>Resultado predecido</h4>
                <img class="team-logo" v-if="winner !== 0" :src="getImgUrl(winnerImage)" alt="">
                <p>{{winnerText}}</p>
            </b-col>
        </b-row>
    </div>
</template>

<script>
import moment from 'moment';

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
        },
        matchStart: {
            type: Date,
            required: true
        },
        winner: {
            type: Number,
            required: true
        }
    },

    data() {
        return {
            
        };
    },

    methods: {
        getImgUrl(pic) {
            return require('@/assets/Logos/' + pic);
        }
    },

    computed: {
        formatedDate() {
            return moment(this.matchStart).format('LLL');
        },

        winnerImage() {
            return (this.winner == 1) ? this.localLogo : this.awayLogo;
        },

        winnerText() {
            if (this.winner === 1) {
                return `Gana ${this.localName}`;
            } else if (this.winner == -1) {
                return `Gana ${this.awayName}`;
            }
            return 'Empate';
        }
    }
}
</script>

<style lang="scss" scoped>
.team-logo {
    width: 4rem;
}

.fixture {
    padding: 1.5rem 0;
    background-color: #38003c;
    color: #ffffff;

    .matchDate {
        display: flex;
        align-items: center;
        justify-content: center;
    }
}

.result {
    background-color: #38003c88;
    color: #ffffff;
}

</style>
