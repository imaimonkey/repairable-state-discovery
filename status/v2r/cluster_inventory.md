# V2R cluster inventory

2026-09-24T03:14:34.530386+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325364674560 available bytes; 81.85% used; 112498308 free inodes.

server1 `/home`: 325364674560 available bytes; 81.85% used; 112498308 free inodes.

server1 `/tmp`: 325364674560 available bytes; 81.85% used; 112498308 free inodes.

server1 `/var/tmp`: 325364674560 available bytes; 81.85% used; 112498308 free inodes.

server1 `/mnt/raid5`: 457903349760 available bytes; 97.90% used; 337732166 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40848818176 available bytes; 97.72% used; 110431209 free inodes.

server2 `/home`: 40848818176 available bytes; 97.72% used; 110431209 free inodes.

server2 `/tmp`: 40848818176 available bytes; 97.72% used; 110431209 free inodes.

server2 `/var/tmp`: 40848818176 available bytes; 97.72% used; 110431209 free inodes.

server2 `/mnt/raid5`: 527629967360 available bytes; 96.35% used; 445198029 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292293165056 available bytes; 83.69% used; 114187092 free inodes.

server3 `/home`: 292293165056 available bytes; 83.69% used; 114187092 free inodes.

server3 `/data`: 39675551744 available bytes; 99.45% used; 225844710 free inodes.

server3 `/tmp`: 292293165056 available bytes; 83.69% used; 114187092 free inodes.

server3 `/var/tmp`: 292293165056 available bytes; 83.69% used; 114187092 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105987805184 available bytes; 94.09% used; 114349621 free inodes.

server4 `/home`: 105987805184 available bytes; 94.09% used; 114349621 free inodes.

server4 `/data`: 289663295488 available bytes; 96.00% used; 225386644 free inodes.

server4 `/tmp`: 105987805184 available bytes; 94.09% used; 114349621 free inodes.

server4 `/var/tmp`: 105987805184 available bytes; 94.09% used; 114349621 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
