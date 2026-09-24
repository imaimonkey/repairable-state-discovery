# V2R cluster inventory

2026-09-24T02:54:07.149274+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325382033408 available bytes; 81.85% used; 112498668 free inodes.

server1 `/home`: 325382033408 available bytes; 81.85% used; 112498668 free inodes.

server1 `/tmp`: 325382033408 available bytes; 81.85% used; 112498668 free inodes.

server1 `/var/tmp`: 325382033408 available bytes; 81.85% used; 112498668 free inodes.

server1 `/mnt/raid5`: 545063845888 available bytes; 97.50% used; 337732341 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40872042496 available bytes; 97.72% used; 110431364 free inodes.

server2 `/home`: 40872042496 available bytes; 97.72% used; 110431364 free inodes.

server2 `/tmp`: 40872042496 available bytes; 97.72% used; 110431364 free inodes.

server2 `/var/tmp`: 40872042496 available bytes; 97.72% used; 110431364 free inodes.

server2 `/mnt/raid5`: 527740735488 available bytes; 96.35% used; 445198912 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292259610624 available bytes; 83.69% used; 114186029 free inodes.

server3 `/home`: 292259610624 available bytes; 83.69% used; 114186029 free inodes.

server3 `/data`: 39731834880 available bytes; 99.45% used; 225845772 free inodes.

server3 `/tmp`: 292259610624 available bytes; 83.69% used; 114186029 free inodes.

server3 `/var/tmp`: 292259610624 available bytes; 83.69% used; 114186029 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106002571264 available bytes; 94.08% used; 114349808 free inodes.

server4 `/home`: 106002571264 available bytes; 94.08% used; 114349808 free inodes.

server4 `/data`: 289731952640 available bytes; 96.00% used; 225386915 free inodes.

server4 `/tmp`: 106002571264 available bytes; 94.08% used; 114349808 free inodes.

server4 `/var/tmp`: 106002571264 available bytes; 94.08% used; 114349808 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
