# V2R cluster inventory

2026-09-27T00:59:35.642623+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315158495232 available bytes; 82.42% used; 112443451 free inodes.

server1 `/home`: 315158495232 available bytes; 82.42% used; 112443451 free inodes.

server1 `/tmp`: 315158495232 available bytes; 82.42% used; 112443451 free inodes.

server1 `/var/tmp`: 315158495232 available bytes; 82.42% used; 112443451 free inodes.

server1 `/mnt/raid5`: 637561167872 available bytes; 97.08% used; 337405785 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17630068736 available bytes; 99.02% used; 110364994 free inodes.

server2 `/home`: 17630068736 available bytes; 99.02% used; 110364994 free inodes.

server2 `/tmp`: 17630068736 available bytes; 99.02% used; 110364994 free inodes.

server2 `/var/tmp`: 17630068736 available bytes; 99.02% used; 110364994 free inodes.

server2 `/mnt/raid5`: 584137936896 available bytes; 95.96% used; 444887303 free inodes.
| server3 | True | ['0', '3'] | [] | reference_compatible=True |

server3 `/`: 79499857920 available bytes; 95.56% used; 114068708 free inodes.

server3 `/home`: 79499857920 available bytes; 95.56% used; 114068708 free inodes.

server3 `/data`: 1342477037568 available bytes; 81.45% used; 225764037 free inodes.

server3 `/tmp`: 79499857920 available bytes; 95.56% used; 114068708 free inodes.

server3 `/var/tmp`: 79499857920 available bytes; 95.56% used; 114068708 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105878581248 available bytes; 94.09% used; 114347835 free inodes.

server4 `/home`: 105878581248 available bytes; 94.09% used; 114347835 free inodes.

server4 `/data`: 406585438208 available bytes; 94.38% used; 224782988 free inodes.

server4 `/tmp`: 105878581248 available bytes; 94.09% used; 114347835 free inodes.

server4 `/var/tmp`: 105878581248 available bytes; 94.09% used; 114347835 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
