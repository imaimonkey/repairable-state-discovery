# V2R cluster inventory

2026-09-27T15:20:42.658026+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 304747106304 available bytes; 83.00% used; 112401390 free inodes.

server1 `/home`: 304747106304 available bytes; 83.00% used; 112401390 free inodes.

server1 `/tmp`: 304747106304 available bytes; 83.00% used; 112401390 free inodes.

server1 `/var/tmp`: 304747106304 available bytes; 83.00% used; 112401390 free inodes.

server1 `/mnt/raid5`: 626092367872 available bytes; 97.13% used; 337424001 free inodes.
| server2 | True | ['5', '6', '7'] | [] |

server2 `/`: 13402734592 available bytes; 99.25% used; 110351754 free inodes.

server2 `/home`: 13402734592 available bytes; 99.25% used; 110351754 free inodes.

server2 `/tmp`: 13402734592 available bytes; 99.25% used; 110351754 free inodes.

server2 `/var/tmp`: 13402734592 available bytes; 99.25% used; 110351754 free inodes.

server2 `/mnt/raid5`: 524174995456 available bytes; 96.38% used; 444720821 free inodes.
| server3 | True | ['0', '1', '2'] | [] |

server3 `/`: 78556925952 available bytes; 95.62% used; 114062763 free inodes.

server3 `/home`: 78556925952 available bytes; 95.62% used; 114062763 free inodes.

server3 `/data`: 1326819999744 available bytes; 81.66% used; 225762849 free inodes.

server3 `/tmp`: 78556925952 available bytes; 95.62% used; 114062763 free inodes.

server3 `/var/tmp`: 78556925952 available bytes; 95.62% used; 114062763 free inodes.
| server4 | True | ['1', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 108536586240 available bytes; 93.94% used; 114372707 free inodes.

server4 `/home`: 108536586240 available bytes; 93.94% used; 114372707 free inodes.

server4 `/data`: 350339776512 available bytes; 95.16% used; 224727147 free inodes.

server4 `/tmp`: 108536586240 available bytes; 93.94% used; 114372707 free inodes.

server4 `/var/tmp`: 108536586240 available bytes; 93.94% used; 114372707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
