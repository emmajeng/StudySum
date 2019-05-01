class AddContentToProfiles < ActiveRecord::Migration[5.2]
  def change
    add_column :profiles, :content, :text
  end
end
