<template>
  <div class="sidebar">
    <div v-show="!collapsed" class="sidebar__nav">
      <ul class="tree">
        <li class="tree__item margin-top-2">
          <div class="tree__link tree__link--group">
            <span class="tree__link-text">{{ template.name }}</span>
          </div>
        </li>
        <component
          :is="getApplicationComponent(application)"
          v-for="application in sortedApplications"
          :key="application.id"
          :application="application"
          :page="page"
          @selected="selectedApplication"
          @selected-page="$emit('selected-page', $event)"
        ></component>
      </ul>
    </div>
    <div class="sidebar__foot">
      <div class="sidebar__logo">
        <Logo height="14" alt="Baserow logo" />
      </div>
      <a class="sidebar__collapse-link" @click="$emit('collapse-toggled')">
        <i
          :class="{
            'iconoir-fast-arrow-right': collapsed,
            'iconoir-fast-arrow-left': !collapsed,
          }"
        ></i>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TemplateSidebar',
  props: {
    template: {
      type: Object,
      required: true,
    },
    applications: {
      type: Array,
      required: true,
    },
    page: {
      required: true,
      validator: (prop) => typeof prop === 'object' || prop === null,
    },
    collapsed: {
      type: Boolean,
      required: true,
    },
  },
  computed: {
    sortedApplications() {
      return this.applications
        .map((a) => a)
        .sort((a, b) => {
          return a.order - b.order
        })
    },
  },
  methods: {
    getApplicationComponent(application) {
      return this.$registry
        .get('application', application.type)
        .getTemplateSidebarComponent()
    },
    selectedApplication(application) {
      this.applications.forEach((app) => {
        app._.selected = application.id === app.id
      })
    },
  },
}
</script>
