class RemoveRoleFromDocuments < ActiveRecord::Migration[5.2]
  def change
    remove_column :documents, :profile_id, :integer
  end
end
