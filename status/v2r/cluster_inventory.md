# V2R cluster inventory

2026-09-24T18:44:34.514002+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324002484224 available bytes; 81.93% used; 112481449 free inodes.

server1 `/home`: 324002484224 available bytes; 81.93% used; 112481449 free inodes.

server1 `/tmp`: 324002484224 available bytes; 81.93% used; 112481449 free inodes.

server1 `/var/tmp`: 324002484224 available bytes; 81.93% used; 112481449 free inodes.

server1 `/mnt/raid5`: 416290963456 available bytes; 98.09% used; 337637713 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 54480039936 available bytes; 96.96% used; 110411941 free inodes.

server2 `/home`: 54480039936 available bytes; 96.96% used; 110411941 free inodes.

server2 `/tmp`: 54480039936 available bytes; 96.96% used; 110411941 free inodes.

server2 `/var/tmp`: 54480039936 available bytes; 96.96% used; 110411941 free inodes.

server2 `/mnt/raid5`: 496275300352 available bytes; 96.57% used; 445160114 free inodes.
| server3 | True | ['1'] | [] |

server3 `/`: 84406452224 available bytes; 95.29% used; 114156135 free inodes.

server3 `/home`: 84406452224 available bytes; 95.29% used; 114156135 free inodes.

server3 `/data`: 132101742592 available bytes; 98.17% used; 225800301 free inodes.

server3 `/tmp`: 84406452224 available bytes; 95.29% used; 114156135 free inodes.

server3 `/var/tmp`: 84406452224 available bytes; 95.29% used; 114156135 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105661652992 available bytes; 94.10% used; 114348497 free inodes.

server4 `/home`: 105661652992 available bytes; 94.10% used; 114348497 free inodes.

server4 `/data`: 90022215680 available bytes; 98.76% used; 225267749 free inodes.

server4 `/tmp`: 105661652992 available bytes; 94.10% used; 114348497 free inodes.

server4 `/var/tmp`: 105661652992 available bytes; 94.10% used; 114348497 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
