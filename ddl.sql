CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    comment TEXT NOT NULL,
    sentiment VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE
);

CREATE OR REPLACE FUNCTION get_user_sentiment_counts(
    p_user_id INT
)
RETURNS TABLE (
    sentiment VARCHAR,
    count BIGINT
) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        c.sentiment,
        COUNT(*)::BIGINT AS count
    FROM 
        comments c
    WHERE 
        c.user_id = p_user_id
    GROUP BY 
        c.sentiment;
END;
$$;