# V2R cluster inventory

2026-09-27T13:45:55.230066+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 304763506688 available bytes; 83.00% used; 112401377 free inodes.

server1 `/home`: 304763506688 available bytes; 83.00% used; 112401377 free inodes.

server1 `/tmp`: 304763506688 available bytes; 83.00% used; 112401377 free inodes.

server1 `/var/tmp`: 304763506688 available bytes; 83.00% used; 112401377 free inodes.

server1 `/mnt/raid5`: 634886803456 available bytes; 97.09% used; 337424247 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 13418471424 available bytes; 99.25% used; 110351822 free inodes.

server2 `/home`: 13418471424 available bytes; 99.25% used; 110351822 free inodes.

server2 `/tmp`: 13418471424 available bytes; 99.25% used; 110351822 free inodes.

server2 `/var/tmp`: 13418471424 available bytes; 99.25% used; 110351822 free inodes.

server2 `/mnt/raid5`: 528287293440 available bytes; 96.35% used; 444732891 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78567292928 available bytes; 95.62% used; 114062769 free inodes.

server3 `/home`: 78567292928 available bytes; 95.62% used; 114062769 free inodes.

server3 `/data`: 1330867904512 available bytes; 81.61% used; 225757390 free inodes.

server3 `/tmp`: 78567292928 available bytes; 95.62% used; 114062769 free inodes.

server3 `/var/tmp`: 78567292928 available bytes; 95.62% used; 114062769 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111009988608 available bytes; 93.81% used; 114372794 free inodes.

server4 `/home`: 111009988608 available bytes; 93.81% used; 114372794 free inodes.

server4 `/data`: 351014002688 available bytes; 95.15% used; 224727481 free inodes.

server4 `/tmp`: 111009988608 available bytes; 93.81% used; 114372794 free inodes.

server4 `/var/tmp`: 111009988608 available bytes; 93.81% used; 114372794 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
