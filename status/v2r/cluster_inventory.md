# V2R cluster inventory

2026-09-25T01:39:14.149835+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319076577280 available bytes; 82.20% used; 112480765 free inodes.

server1 `/home`: 319076577280 available bytes; 82.20% used; 112480765 free inodes.

server1 `/tmp`: 319076577280 available bytes; 82.20% used; 112480765 free inodes.

server1 `/var/tmp`: 319076577280 available bytes; 82.20% used; 112480765 free inodes.

server1 `/mnt/raid5`: 416466006016 available bytes; 98.09% used; 337611882 free inodes.
| server2 | True | ['2', '3', '6'] | [] | reference_compatible=False |

server2 `/`: 23048339456 available bytes; 98.71% used; 110410772 free inodes.

server2 `/home`: 23048339456 available bytes; 98.71% used; 110410772 free inodes.

server2 `/tmp`: 23048339456 available bytes; 98.71% used; 110410772 free inodes.

server2 `/var/tmp`: 23048339456 available bytes; 98.71% used; 110410772 free inodes.

server2 `/mnt/raid5`: 490279972864 available bytes; 96.61% used; 445161073 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84353650688 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84353650688 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 146537742336 available bytes; 97.97% used; 225812125 free inodes.

server3 `/tmp`: 84353650688 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84353650688 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105778630656 available bytes; 94.10% used; 114348287 free inodes.

server4 `/home`: 105778630656 available bytes; 94.10% used; 114348287 free inodes.

server4 `/data`: 53313949696 available bytes; 99.26% used; 225030611 free inodes.

server4 `/tmp`: 105778630656 available bytes; 94.10% used; 114348287 free inodes.

server4 `/var/tmp`: 105778630656 available bytes; 94.10% used; 114348287 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
