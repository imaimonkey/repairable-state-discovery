# V2R cluster inventory

2026-09-24T04:52:46.614760+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324620521472 available bytes; 81.89% used; 112492789 free inodes.

server1 `/home`: 324620521472 available bytes; 81.89% used; 112492789 free inodes.

server1 `/tmp`: 324620521472 available bytes; 81.89% used; 112492789 free inodes.

server1 `/var/tmp`: 324620521472 available bytes; 81.89% used; 112492789 free inodes.

server1 `/mnt/raid5`: 474676699136 available bytes; 97.82% used; 337724585 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40767369216 available bytes; 97.73% used; 110430446 free inodes.

server2 `/home`: 40767369216 available bytes; 97.73% used; 110430446 free inodes.

server2 `/tmp`: 40767369216 available bytes; 97.73% used; 110430446 free inodes.

server2 `/var/tmp`: 40767369216 available bytes; 97.73% used; 110430446 free inodes.

server2 `/mnt/raid5`: 523812794368 available bytes; 96.38% used; 445194971 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292378869760 available bytes; 83.68% used; 114199891 free inodes.

server3 `/home`: 292378869760 available bytes; 83.68% used; 114199891 free inodes.

server3 `/data`: 24355098624 available bytes; 99.66% used; 225840556 free inodes.

server3 `/tmp`: 292378869760 available bytes; 83.68% used; 114199891 free inodes.

server3 `/var/tmp`: 292378869760 available bytes; 83.68% used; 114199891 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105835839488 available bytes; 94.09% used; 114349396 free inodes.

server4 `/home`: 105835839488 available bytes; 94.09% used; 114349396 free inodes.

server4 `/data`: 253350928384 available bytes; 96.50% used; 225366837 free inodes.

server4 `/tmp`: 105835839488 available bytes; 94.09% used; 114349396 free inodes.

server4 `/var/tmp`: 105835839488 available bytes; 94.09% used; 114349396 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
