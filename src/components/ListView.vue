<template>
  <div class="list-container">
    <ul class="main-list" v-if="Object.keys(results).length > 0 || Object.keys(selection).length > 0">
      <ul
        class="sub-list"
        v-for="[pdf, pages] in Object.entries(results)"
        :key="pdf"
      >
        <li class="pdf-object">
          <h1 class="pdf-path">
            {{ pdf }}
          </h1>
          <div>
            <button class="add-btn" @click="addPdf(pdf)"></button>
          </div>
        </li>

        <li class="page-object" v-for="page in pages" :key="page.page" @click="viewPage(page)">
          <h1 class="page-number">
            {{ page.page }}
          </h1>
          <div>
            <button class="add-btn" @click="addPage(page)"></button>
          </div>
        </li>
      </ul>
    </ul>

    <ul class="selected-list" v-if="Object.keys(selected).length > 0">
      <ul
        class="sub-list"
        v-for="[pdf, pages] in Object.entries(selected)"
        :key="pdf"
      >
        <li class="pdf-object">
          <h1 class="pdf-path">
            {{ pdf }}
          </h1>
          <div>
            <button class="remove-btn" @click="removePdf(pdf)"></button>
          </div>
        </li>

        <li class="page-object" v-for="page in pages" :key="page.page">
          <h1 class="page-number">
            {{ page.page }}
          </h1>
          <div>
            <button class="remove-btn" @click="removePage(page)"></button>
          </div>
        </li>
      </ul>
    </ul>
  </div>
</template>
<script>
export default {
  props: {
    matches: {
      type: Object,
      required: true,
    },
    selection: {
      type: Object,
      required: true,
    },
  },
  watch: {
    matches() {
      this.selected = {};
      this.results = this.matches;
    },
    selection() {
      this.selected = this.selection;
      console.log(this.selected);
    },
  },
  data() {
    return {
      selected: {},
      results: {},
    };
  },
  mounted() {},
  methods: {
    addPage(page) {
      const pdf = page.pdf;
      // remove the page from the results
      const pdfPages = this.results[pdf];
      const index = pdfPages.indexOf(page);
      pdfPages.splice(index, 1);
      if (pdfPages.length === 0) {
        delete this.results[pdf];
      }

      // add the page to the selection
      this.$emit("add-page", page);
    },
    removePage(page) {
      const pdf = page.pdf;
      // add the page back to the results
      if (pdf in this.results) {
        this.results[pdf].push(page);
      } else {
        this.results[pdf] = [page];
      }
      // remove the page from the selection
      this.$emit("remove-page", page);
    },
    viewPage(page){
      this.$emit("view-page", page);
    }
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
  background-color: #72967f;
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
