<template>
  <div class="list-container">
    <list-section
      v-if="
        Object.keys(benched).length > 0 ||
        Object.keys(active).length > 0
      "
      :type="'unselected'"
      :items="benched"
      @add="addPagesToSelected"
    />

    <list-section
      v-if="Object.keys(active).length > 0"
      :type="'selected'"
      :items="active"
      @remove="removePagesFromSelected"
    />
  </div>
</template>

<script>
import ListSection from "@/components/ListSection"; // Adjust the path based on your project structure

export default {
  props: {
    allResults: {
      type: Object,
      required: true,
    },
    activeResults: {
      type: Object,
      required: true,
    },
    benchedResults:{
      type: Object,
      required: true,
    },
  },

  data() {
    return {
      active: {},
      benched: {},
    };
  },

  watch: {
    allResults() {
      console.log("allResults changed", JSON.stringify(this.allResults));
      this.active = {};
      this.benched = this.allResults;
    },
    activeResults() {
      console.log("activeResults changed", JSON.stringify(this.activeResults));
      this.active = this.activeResults;
    },
    benchedResults() {
      console.log("benchedResults changed", JSON.stringify(this.benchedResults));
      this.benched = this.benchedResults;
    },
  },

  methods: {
    addPagesToSelected(pages) {
      this.$emit("add-pages", pages);
    },
    removePagesFromSelected(pages) {
      this.$emit("remove-pages", pages);
    },
  },

  components: {
    ListSection,
  },
};
</script>

<style>
h1 {
  margin: 0;
  padding: 10px;
  font-size: 0.8rem;
  font-weight: normal;
  text-align: left;
}

.list-container {
  display: flex;
  flex-direction: row;
}

.main-list {
  width: 50%;
  padding: 0;
  justify-self: left;
}

.selected-list {
  width: 50%;
  padding: 0;
  justify-self: right;
}

.sub-list {
  text-align: center;
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
}

.pdf-object {
  height: fit-content;
  cursor: pointer;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  border: 1px solid rgba(144, 144, 144, 0.393);
  border-radius: 5px;
  box-shadow: 1px 1px 3px rgba(83, 83, 83, 0.445);
  background: #444;
  margin: 5px;
}

.pdf-path {
  width: 75%;
  word-wrap: break-word;
}

.page-object {
  cursor: pointer;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  border: 1px solid rgba(144, 144, 144, 0.393);
  border-radius: 5px;
  box-shadow: 1px 1px 3px rgba(83, 83, 83, 0.445);
  background: #444;
  margin: 5px;
  margin-left: 50px;
}

.page-object .page-number {
  color: rgb(255, 255, 255);
  font-weight: bold;
}

.add-btn {
  width: 20px;
  height: 20px;
  border-radius: 10px;
  border: none;
  background: #1ab553;
  cursor: pointer;
  margin: 0 5px;
}

.add-btn:hover {
  background: #1d743d;
  border: 1px solid #8baa96;
}

.remove-btn {
  width: 20px;
  height: 20px;
  border: none;
  border-radius: 10px;
  border: none;
  background: #b51a1a;
  cursor: pointer;
  margin: 0 5px;
}

.remove-btn:hover {
  background: #741d1d;
  border: 1px solid #aa8b8b;
}
</style>
