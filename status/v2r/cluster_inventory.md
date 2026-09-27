# V2R cluster inventory

2026-09-27T13:56:42.346422+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304763367424 available bytes; 83.00% used; 112401383 free inodes.

server1 `/home`: 304763367424 available bytes; 83.00% used; 112401383 free inodes.

server1 `/tmp`: 304763367424 available bytes; 83.00% used; 112401383 free inodes.

server1 `/var/tmp`: 304763367424 available bytes; 83.00% used; 112401383 free inodes.

server1 `/mnt/raid5`: 634875203584 available bytes; 97.09% used; 337424252 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 13416382464 available bytes; 99.25% used; 110351820 free inodes.

server2 `/home`: 13416382464 available bytes; 99.25% used; 110351820 free inodes.

server2 `/tmp`: 13416382464 available bytes; 99.25% used; 110351820 free inodes.

server2 `/var/tmp`: 13416382464 available bytes; 99.25% used; 110351820 free inodes.

server2 `/mnt/raid5`: 527924727808 available bytes; 96.35% used; 444732394 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78560063488 available bytes; 95.62% used; 114062773 free inodes.

server3 `/home`: 78560063488 available bytes; 95.62% used; 114062773 free inodes.

server3 `/data`: 1330872274944 available bytes; 81.61% used; 225757254 free inodes.

server3 `/tmp`: 78560063488 available bytes; 95.62% used; 114062773 free inodes.

server3 `/var/tmp`: 78560063488 available bytes; 95.62% used; 114062773 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111009828864 available bytes; 93.81% used; 114372795 free inodes.

server4 `/home`: 111009828864 available bytes; 93.81% used; 114372795 free inodes.

server4 `/data`: 350883635200 available bytes; 95.15% used; 224727462 free inodes.

server4 `/tmp`: 111009828864 available bytes; 93.81% used; 114372795 free inodes.

server4 `/var/tmp`: 111009828864 available bytes; 93.81% used; 114372795 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
