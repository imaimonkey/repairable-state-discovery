# V2R cluster inventory

2026-09-27T11:53:08.159999+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304696127488 available bytes; 83.00% used; 112401614 free inodes.

server1 `/home`: 304696127488 available bytes; 83.00% used; 112401614 free inodes.

server1 `/tmp`: 304696127488 available bytes; 83.00% used; 112401614 free inodes.

server1 `/var/tmp`: 304696127488 available bytes; 83.00% used; 112401614 free inodes.

server1 `/mnt/raid5`: 634687139840 available bytes; 97.09% used; 337424396 free inodes.
| server2 | True | ['0', '1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16416997376 available bytes; 99.08% used; 110353088 free inodes.

server2 `/home`: 16416997376 available bytes; 99.08% used; 110353088 free inodes.

server2 `/tmp`: 16416997376 available bytes; 99.08% used; 110353088 free inodes.

server2 `/var/tmp`: 16416997376 available bytes; 99.08% used; 110353088 free inodes.

server2 `/mnt/raid5`: 569526222848 available bytes; 96.06% used; 444736304 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78546776064 available bytes; 95.62% used; 114062802 free inodes.

server3 `/home`: 78546776064 available bytes; 95.62% used; 114062802 free inodes.

server3 `/data`: 1331867918336 available bytes; 81.59% used; 225759070 free inodes.

server3 `/tmp`: 78546776064 available bytes; 95.62% used; 114062802 free inodes.

server3 `/var/tmp`: 78546776064 available bytes; 95.62% used; 114062802 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111029563392 available bytes; 93.80% used; 114372817 free inodes.

server4 `/home`: 111029563392 available bytes; 93.80% used; 114372817 free inodes.

server4 `/data`: 352939278336 available bytes; 95.12% used; 224728079 free inodes.

server4 `/tmp`: 111029563392 available bytes; 93.80% used; 114372817 free inodes.

server4 `/var/tmp`: 111029563392 available bytes; 93.80% used; 114372817 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
