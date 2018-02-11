<template>
  <div id="players_table">

    <v-card fluid>
      <v-card-title>
        <h3 style="font-weight:400">The data is based on the first <span style="font-weight:600">1000</span> teams</h3>
      </v-card-title>
      <v-data-table :headers="headers" must-sort :items="items" hide-actions class="elevation-1" :loading="loading" v-bind:pagination.sync="pagination"   
      >
      <template slot="items" slot-scope="props">
        <td class="text-xs-right">{{ Math.round(props.item.captain_by/1000 * 100* 10 ) / 10 }}%</td>
        <td class="text-xs-right">{{ Math.round(props.item.selected_by/1000 * 100* 10 ) / 10 }}%</td>
        <td class="text-xs-right">{{ props.item.team }}</td>
        <td class="text-xs-right">{{ props.item.points_value }}</td>
        <td class="text-xs-right">{{ getPosition(props.item.position) }}</td>
        <td class="text-xs-right">{{ props.item.player_market_value }}</td>
        <td class="text-xs-right"> {{ props.item.player_name }}</td>
        <td class="text-xs-right">
     <!--      <a target="_blank" v-for="team in props.item.teams_captain" :href="'http://dreamteam.sport5.co.il/#!/MyTeam/' + team.id">
            {{team.id}}
          </a> -->
        </td>
      </template>
    </v-data-table>
    </v-card>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'PlayersTable',
  components: {
  },
  methods: {
    ...mapActions([
      'pullPlayers'
    ]),
    getPosition (pos) {
      if (pos === 'm') {
        return 'קשר'
      } else if (pos === 'a') {
        return 'חלוץ'
      } else if (pos === 'g') {
        return 'שוער'
      } else if (pos === 'd') {
        return 'מגן'
      }
    }
  },
  computed: {
  },
  created () {
    console.log('created!')
    this.loading = true
    this.pullPlayers().then((res) => {
      if (res.error) {
        console.log('we got error')
      } else {
        console.log('res:', res.data.players)
        this.items = res.data.players
      }
      this.loading = false
    })
  },
  data () {
    return {
      search: '',
      pagination: {
        sortBy: 'captain_by',
        page: 1,
        rowsPerPage: 500,
        descending: true,
        totalItems: 0
      },
      loading: true,
      headers: [
        { text: 'Captain', value: 'captain_by' },
        { text: 'Selected By', value: 'selected_by' },
        { text: 'Team', value: 'team' },
        { text: 'Total Points', value: 'points_value' },
        { text: 'Position', value: 'position' },
        { text: 'Price', value: 'player_market_value' },
        { text: 'Player name', value: 'player_name' },
        { text: 'Teams', value: 'teams_captain' }
      ],
      items: []
    }
  }
}
</script>

<style scoped>
  #players_table{}
</style>
