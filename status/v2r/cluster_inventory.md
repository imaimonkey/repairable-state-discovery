# V2R cluster inventory

2026-09-23T16:07:53.586772+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41411084288 available bytes; 97.69% used; 110435187 free inodes.

server2 `/home`: 41411084288 available bytes; 97.69% used; 110435187 free inodes.

server2 `/tmp`: 41411084288 available bytes; 97.69% used; 110435187 free inodes.

server2 `/var/tmp`: 41411084288 available bytes; 97.69% used; 110435187 free inodes.

server2 `/mnt/raid5`: 549457629184 available bytes; 96.20% used; 445218416 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 340498313216 available bytes; 81.00% used; 114296137 free inodes.

server3 `/home`: 340498243584 available bytes; 81.00% used; 114296137 free inodes.

server3 `/data`: 125329895424 available bytes; 98.27% used; 225854489 free inodes.

server3 `/tmp`: 340498173952 available bytes; 81.00% used; 114296137 free inodes.

server3 `/var/tmp`: 340498141184 available bytes; 81.00% used; 114296137 free inodes.
| server4 | True | ['3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111498977280 available bytes; 93.78% used; 114375780 free inodes.

server4 `/home`: 111498977280 available bytes; 93.78% used; 114375780 free inodes.

server4 `/data`: 37443043328 available bytes; 99.48% used; 225486574 free inodes.

server4 `/tmp`: 111498977280 available bytes; 93.78% used; 114375780 free inodes.

server4 `/var/tmp`: 111498977280 available bytes; 93.78% used; 114375780 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
