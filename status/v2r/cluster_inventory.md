# V2R cluster inventory

2026-09-24T00:52:35.302637+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 325530931200 available bytes; 81.84% used; 112500354 free inodes.

server1 `/home`: 325530931200 available bytes; 81.84% used; 112500354 free inodes.

server1 `/tmp`: 325530931200 available bytes; 81.84% used; 112500354 free inodes.

server1 `/var/tmp`: 325530931200 available bytes; 81.84% used; 112500354 free inodes.

server1 `/mnt/raid5`: 1051095691264 available bytes; 95.18% used; 337734738 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40981356544 available bytes; 97.71% used; 110432252 free inodes.

server2 `/home`: 40981356544 available bytes; 97.71% used; 110432252 free inodes.

server2 `/tmp`: 40981356544 available bytes; 97.71% used; 110432252 free inodes.

server2 `/var/tmp`: 40981356544 available bytes; 97.71% used; 110432252 free inodes.

server2 `/mnt/raid5`: 532080381952 available bytes; 96.32% used; 445202546 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292346626048 available bytes; 83.69% used; 114189056 free inodes.

server3 `/home`: 292346626048 available bytes; 83.69% used; 114189056 free inodes.

server3 `/data`: 82164678656 available bytes; 98.86% used; 225843438 free inodes.

server3 `/tmp`: 292346626048 available bytes; 83.69% used; 114189056 free inodes.

server3 `/var/tmp`: 292346626048 available bytes; 83.69% used; 114189056 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106033446912 available bytes; 94.08% used; 114349749 free inodes.

server4 `/home`: 106033446912 available bytes; 94.08% used; 114349749 free inodes.

server4 `/data`: 292878200832 available bytes; 95.95% used; 225414554 free inodes.

server4 `/tmp`: 106033446912 available bytes; 94.08% used; 114349749 free inodes.

server4 `/var/tmp`: 106033446912 available bytes; 94.08% used; 114349749 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
