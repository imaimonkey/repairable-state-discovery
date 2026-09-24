# V2R cluster inventory

2026-09-24T12:11:26.175146+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 322684456960 available bytes; 82.00% used; 112464399 free inodes.

server1 `/home`: 322684456960 available bytes; 82.00% used; 112464399 free inodes.

server1 `/tmp`: 322684456960 available bytes; 82.00% used; 112464399 free inodes.

server1 `/var/tmp`: 322684456960 available bytes; 82.00% used; 112464399 free inodes.

server1 `/mnt/raid5`: 405241389056 available bytes; 98.14% used; 337684575 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57620439040 available bytes; 96.79% used; 110429590 free inodes.

server2 `/home`: 57620439040 available bytes; 96.79% used; 110429590 free inodes.

server2 `/tmp`: 57620439040 available bytes; 96.79% used; 110429590 free inodes.

server2 `/var/tmp`: 57620439040 available bytes; 96.79% used; 110429590 free inodes.

server2 `/mnt/raid5`: 509075734528 available bytes; 96.48% used; 445172325 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85323657216 available bytes; 95.24% used; 114172960 free inodes.

server3 `/home`: 85323657216 available bytes; 95.24% used; 114172960 free inodes.

server3 `/data`: 163516231680 available bytes; 97.74% used; 225815466 free inodes.

server3 `/tmp`: 85323657216 available bytes; 95.24% used; 114172960 free inodes.

server3 `/var/tmp`: 85323657216 available bytes; 95.24% used; 114172960 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105781452800 available bytes; 94.10% used; 114348816 free inodes.

server4 `/home`: 105781452800 available bytes; 94.10% used; 114348816 free inodes.

server4 `/data`: 90426544128 available bytes; 98.75% used; 225257316 free inodes.

server4 `/tmp`: 105781452800 available bytes; 94.10% used; 114348816 free inodes.

server4 `/var/tmp`: 105781452800 available bytes; 94.10% used; 114348816 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
