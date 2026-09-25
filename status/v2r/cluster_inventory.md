# V2R cluster inventory

2026-09-25T09:36:38.258300+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318836813824 available bytes; 82.21% used; 112480386 free inodes.

server1 `/home`: 318836813824 available bytes; 82.21% used; 112480386 free inodes.

server1 `/tmp`: 318836813824 available bytes; 82.21% used; 112480386 free inodes.

server1 `/var/tmp`: 318836813824 available bytes; 82.21% used; 112480386 free inodes.

server1 `/mnt/raid5`: 350372696064 available bytes; 98.39% used; 337556867 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22827855872 available bytes; 98.73% used; 110410484 free inodes.

server2 `/home`: 22827855872 available bytes; 98.73% used; 110410484 free inodes.

server2 `/tmp`: 22827855872 available bytes; 98.73% used; 110410484 free inodes.

server2 `/var/tmp`: 22827855872 available bytes; 98.73% used; 110410484 free inodes.

server2 `/mnt/raid5`: 331549773824 available bytes; 97.71% used; 445092357 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84418703360 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84418703360 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 142299820032 available bytes; 98.03% used; 225810553 free inodes.

server3 `/tmp`: 84418703360 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84418703360 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105623560192 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105623560192 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 241720401920 available bytes; 96.66% used; 224994722 free inodes.

server4 `/tmp`: 105623560192 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105623560192 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
