-- :name upsert_publication :insert
INSERT INTO publication
  (publication_id, producer_id, canonical_url, title, publication_text, published_at, first_seen_at, last_updated_at, urls, hashtags, keywords, tags, metadata, comments, version, author, connect_from)
VALUES
  (:publication_id, :producer_id, :canonical_url, :title, :publication_text, :published_at, :first_seen_at, :last_updated_at, :urls, :hashtags, :keywords, :tags, :metadata, :comments, :version, :author, :connect_from)
ON DUPLICATE KEY UPDATE
  canonical_url = :canonical_url, title = :title, publication_text = :publication_text, published_at = :published_at, first_seen_at = :first_seen_at, last_updated_at = :last_updated_at, urls = :urls, hashtags = :hashtags, keywords = :keywords, tags = :tags, metadata = :metadata, comments = :comments, author = :author, connect_from = :connect_from