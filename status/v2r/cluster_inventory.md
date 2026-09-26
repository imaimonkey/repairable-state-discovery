# V2R cluster inventory

2026-09-26T12:22:32.811844+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318183370752 available bytes; 82.25% used; 112474768 free inodes.

server1 `/home`: 318183370752 available bytes; 82.25% used; 112474768 free inodes.

server1 `/tmp`: 318183370752 available bytes; 82.25% used; 112474768 free inodes.

server1 `/var/tmp`: 318183370752 available bytes; 82.25% used; 112474768 free inodes.

server1 `/mnt/raid5`: 218574430208 available bytes; 99.00% used; 337537834 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19786371072 available bytes; 98.90% used; 110383628 free inodes.

server2 `/home`: 19786371072 available bytes; 98.90% used; 110383628 free inodes.

server2 `/tmp`: 19786371072 available bytes; 98.90% used; 110383628 free inodes.

server2 `/var/tmp`: 19786371072 available bytes; 98.90% used; 110383628 free inodes.

server2 `/mnt/raid5`: 240527831040 available bytes; 98.34% used; 444980520 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82649214976 available bytes; 95.39% used; 114110828 free inodes.

server3 `/home`: 82649214976 available bytes; 95.39% used; 114110828 free inodes.

server3 `/data`: 123423129600 available bytes; 98.29% used; 225824204 free inodes.

server3 `/tmp`: 82649214976 available bytes; 95.39% used; 114110828 free inodes.

server3 `/var/tmp`: 82649214976 available bytes; 95.39% used; 114110828 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105899909120 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105899909120 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 88577425408 available bytes; 98.78% used; 224879220 free inodes.

server4 `/tmp`: 105899909120 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105899909120 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
