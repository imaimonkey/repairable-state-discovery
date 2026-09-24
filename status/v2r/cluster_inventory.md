# V2R cluster inventory

2026-09-24T11:54:18.202912+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324291727360 available bytes; 81.91% used; 112488480 free inodes.

server1 `/home`: 324291727360 available bytes; 81.91% used; 112488480 free inodes.

server1 `/tmp`: 324291727360 available bytes; 81.91% used; 112488480 free inodes.

server1 `/var/tmp`: 324291727360 available bytes; 81.91% used; 112488480 free inodes.

server1 `/mnt/raid5`: 415353671680 available bytes; 98.09% used; 337686348 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57635328000 available bytes; 96.78% used; 110429756 free inodes.

server2 `/home`: 57635328000 available bytes; 96.78% used; 110429756 free inodes.

server2 `/tmp`: 57635328000 available bytes; 96.78% used; 110429756 free inodes.

server2 `/var/tmp`: 57635328000 available bytes; 96.78% used; 110429756 free inodes.

server2 `/mnt/raid5`: 509899206656 available bytes; 96.48% used; 445172477 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85754568704 available bytes; 95.21% used; 114198466 free inodes.

server3 `/home`: 85754568704 available bytes; 95.21% used; 114198466 free inodes.

server3 `/data`: 163632205824 available bytes; 97.74% used; 225815793 free inodes.

server3 `/tmp`: 85754568704 available bytes; 95.21% used; 114198466 free inodes.

server3 `/var/tmp`: 85754568704 available bytes; 95.21% used; 114198466 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105727328256 available bytes; 94.10% used; 114348830 free inodes.

server4 `/home`: 105727328256 available bytes; 94.10% used; 114348830 free inodes.

server4 `/data`: 115381760000 available bytes; 98.41% used; 225257898 free inodes.

server4 `/tmp`: 105727328256 available bytes; 94.10% used; 114348830 free inodes.

server4 `/var/tmp`: 105727328256 available bytes; 94.10% used; 114348830 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
