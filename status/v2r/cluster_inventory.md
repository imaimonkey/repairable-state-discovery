# V2R cluster inventory

2026-09-27T10:17:09.517755+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314441015296 available bytes; 82.46% used; 112440680 free inodes.

server1 `/home`: 314441015296 available bytes; 82.46% used; 112440680 free inodes.

server1 `/tmp`: 314441015296 available bytes; 82.46% used; 112440680 free inodes.

server1 `/var/tmp`: 314441015296 available bytes; 82.46% used; 112440680 free inodes.

server1 `/mnt/raid5`: 635420721152 available bytes; 97.09% used; 337424412 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16512335872 available bytes; 99.08% used; 110356612 free inodes.

server2 `/home`: 16512335872 available bytes; 99.08% used; 110356612 free inodes.

server2 `/tmp`: 16512335872 available bytes; 99.08% used; 110356612 free inodes.

server2 `/var/tmp`: 16512335872 available bytes; 99.08% used; 110356612 free inodes.

server2 `/mnt/raid5`: 572155076608 available bytes; 96.05% used; 444739542 free inodes.
| server3 | True | ['0', '2'] | [] | reference_compatible=True |

server3 `/`: 78544416768 available bytes; 95.62% used; 114062836 free inodes.

server3 `/home`: 78544416768 available bytes; 95.62% used; 114062836 free inodes.

server3 `/data`: 1332197486592 available bytes; 81.59% used; 225761139 free inodes.

server3 `/tmp`: 78544416768 available bytes; 95.62% used; 114062836 free inodes.

server3 `/var/tmp`: 78544416768 available bytes; 95.62% used; 114062836 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111040647168 available bytes; 93.80% used; 114372831 free inodes.

server4 `/home`: 111040647168 available bytes; 93.80% used; 114372831 free inodes.

server4 `/data`: 363776417792 available bytes; 94.97% used; 224766934 free inodes.

server4 `/tmp`: 111040647168 available bytes; 93.80% used; 114372831 free inodes.

server4 `/var/tmp`: 111040647168 available bytes; 93.80% used; 114372831 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
