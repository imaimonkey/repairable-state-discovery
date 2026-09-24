# V2R cluster inventory

2026-09-24T05:46:16.907521+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324525891584 available bytes; 81.90% used; 112492105 free inodes.

server1 `/home`: 324525891584 available bytes; 81.90% used; 112492105 free inodes.

server1 `/tmp`: 324525891584 available bytes; 81.90% used; 112492105 free inodes.

server1 `/var/tmp`: 324525891584 available bytes; 81.90% used; 112492105 free inodes.

server1 `/mnt/raid5`: 517614575616 available bytes; 97.63% used; 337723919 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57908506624 available bytes; 96.77% used; 110431330 free inodes.

server2 `/home`: 57908506624 available bytes; 96.77% used; 110431330 free inodes.

server2 `/tmp`: 57908506624 available bytes; 96.77% used; 110431330 free inodes.

server2 `/var/tmp`: 57908506624 available bytes; 96.77% used; 110431330 free inodes.

server2 `/mnt/raid5`: 521877286912 available bytes; 96.39% used; 445193394 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 126746902528 available bytes; 92.93% used; 114171769 free inodes.

server3 `/home`: 126746902528 available bytes; 92.93% used; 114171769 free inodes.

server3 `/data`: 185232486400 available bytes; 97.44% used; 225839035 free inodes.

server3 `/tmp`: 126746902528 available bytes; 92.93% used; 114171769 free inodes.

server3 `/var/tmp`: 126746902528 available bytes; 92.93% used; 114171769 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105816203264 available bytes; 94.10% used; 114349351 free inodes.

server4 `/home`: 105816203264 available bytes; 94.10% used; 114349351 free inodes.

server4 `/data`: 251477417984 available bytes; 96.52% used; 225358018 free inodes.

server4 `/tmp`: 105816203264 available bytes; 94.10% used; 114349351 free inodes.

server4 `/var/tmp`: 105816203264 available bytes; 94.10% used; 114349351 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
