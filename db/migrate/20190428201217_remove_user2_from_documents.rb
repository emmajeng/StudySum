class RemoveUser2FromDocuments < ActiveRecord::Migration[5.2]
  def change
    remove_column :documents, :users, :reference
  end
end
