class AddProfileIdToDocument < ActiveRecord::Migration[5.2]
  def change
    add_column :documents, :profile_id, :integer
  end
end
