<template>
  <form @submit.prevent="submit">
    <FormElement :error="fieldHasErrors('name')" class="control">
      <label class="control__label">
        <i class="iconoira-text"></i>
        {{ $t('applicationForm.nameLabel') }}
      </label>
      <div class="control__elements">
        <input
          ref="name"
          v-model="values.name"
          :class="{ 'input--error': fieldHasErrors('name') }"
          type="text"
          class="input"
          @focus.once="$event.target.select()"
          @blur="$v.values.name.$touch()"
        />
        <div v-if="fieldHasErrors('name')" class="error">
          {{ $t('error.requiredField') }}
        </div>
      </div>
    </FormElement>
    <div class="actions">
      <div class="align-right">
        <Button
          type="primary"
          size="large"
          :loading="loading"
          :disabled="loading"
        >
          {{ $t('action.add') }}
          {{ databaseApplicationType.getName() | lowercase }}
        </Button>
      </div>
    </div>
  </form>
</template>

<script>
import form from '@baserow/modules/core/mixins/form'
import { required } from 'vuelidate/lib/validators'

export default {
  name: 'BlankDatabaseForm',
  mixins: [form],
  props: {
    defaultName: {
      type: String,
      required: false,
      default: '',
    },
    loading: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      values: {
        name: this.defaultName,
      },
    }
  },
  computed: {
    databaseApplicationType() {
      return this.$registry.get('application', 'database')
    },
  },
  mounted() {
    this.$refs.name.focus()
  },
  validations: {
    values: {
      name: { required },
    },
  },
}
</script>
