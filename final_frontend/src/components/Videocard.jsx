const VideoCard = ({ video, onVideoClick, size, showDescription }) => {
    console.log(video)
    return (
      <div className="video-card">
        {/* Thumbnail Section */}
        <div className="thumbnail-container">
          <img src={'http://localhost:8000/'+video.thumbnail} alt={video.title} />
          {/* <span className="duration-badge">{formatDuration(video.duration)}</span> */}
          <span className="views-badge">{video.views}</span>
        </div>
        
        {/* Content Section */}
        <div className="content-section">
          <h3 className="video-title">{video.title}</h3>
          <p className="video-stats">
            {video.views} views • {video.created_at}
          </p>
          {showDescription && (
            <p className="description">{video.description}</p>
          )}
        </div>
      </div>
    )
  }

  export default VideoCard