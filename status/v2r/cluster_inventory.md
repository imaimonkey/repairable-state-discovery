# V2R cluster inventory

2026-09-27T02:05:05.638665+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315158896640 available bytes; 82.42% used; 112443314 free inodes.

server1 `/home`: 315158896640 available bytes; 82.42% used; 112443314 free inodes.

server1 `/tmp`: 315158896640 available bytes; 82.42% used; 112443314 free inodes.

server1 `/var/tmp`: 315158896640 available bytes; 82.42% used; 112443314 free inodes.

server1 `/mnt/raid5`: 637477490688 available bytes; 97.08% used; 337405437 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17628237824 available bytes; 99.02% used; 110364994 free inodes.

server2 `/home`: 17628237824 available bytes; 99.02% used; 110364994 free inodes.

server2 `/tmp`: 17628237824 available bytes; 99.02% used; 110364994 free inodes.

server2 `/var/tmp`: 17628237824 available bytes; 99.02% used; 110364994 free inodes.

server2 `/mnt/raid5`: 581154775040 available bytes; 95.98% used; 444885644 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78714777600 available bytes; 95.61% used; 114062951 free inodes.

server3 `/home`: 78714777600 available bytes; 95.61% used; 114062951 free inodes.

server3 `/data`: 1338763010048 available bytes; 81.50% used; 225762677 free inodes.

server3 `/tmp`: 78714777600 available bytes; 95.61% used; 114062951 free inodes.

server3 `/var/tmp`: 78714777600 available bytes; 95.61% used; 114062951 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105859821568 available bytes; 94.09% used; 114347763 free inodes.

server4 `/home`: 105859821568 available bytes; 94.09% used; 114347763 free inodes.

server4 `/data`: 403634778112 available bytes; 94.42% used; 224782317 free inodes.

server4 `/tmp`: 105859821568 available bytes; 94.09% used; 114347763 free inodes.

server4 `/var/tmp`: 105859821568 available bytes; 94.09% used; 114347763 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
