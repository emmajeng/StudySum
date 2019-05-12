class AddTypeToInput < ActiveRecord::Migration[5.2]
  def change
    add_column :inputs, :inputType, :string
  end
end
