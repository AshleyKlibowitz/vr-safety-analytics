-- QUERY 1: High-Risk Asset Identification
-- Identify which 3D assets are most correlated with user reports.
SELECT 
    t.asset_used,
    COUNT(t.event_id) as total_uses,
    COUNT(r.report_id) as report_count,
    -- Calculate Risk Score: (Reports / Uses) * 100
    ROUND((CAST(COUNT(r.report_id) AS FLOAT) / COUNT(t.event_id)) * 100, 2) as risk_score
FROM telemetry t
LEFT JOIN reports r 
    ON t.session_id = r.session_id 
    AND t.user_id = r.reported_user_id
GROUP BY t.asset_used
ORDER BY risk_score DESC;

-- QUERY 2: Voice Toxicity Threshold
-- Find the average volume of users who get reported vs those who don't.
SELECT 
    CASE 
        WHEN r.report_id IS NOT NULL THEN 'Reported Users'
        ELSE 'Safe Users'
    END as user_status,
    ROUND(AVG(t.voice_volume_db), 1) as avg_volume_db,
    COUNT(*) as event_count
FROM telemetry t
LEFT JOIN reports r 
    ON t.session_id = r.session_id
GROUP BY user_status;