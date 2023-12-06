DO $$
BEGIN
    FOR season IN 2..3 LOOP
        FOR episode IN 1..5 LOOP
            INSERT INTO Episodes (episode_id, season, episode) VALUES (season * 100 + episode, season, episode);
        END LOOP;
    END LOOP;
END $$;


